"""CSCA08 Fall 2023 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2023 Jacqueline Smith and Anya Tafliovich.

"""

from constants import (YR, MON, DAY, DEP, ARR, ROW, SEAT, FFN,
                       WINDOW, AISLE, MIDDLE, SA, SB, SC, SD, SE, SF)


# We provide this function solution as an example of correct function
# documentation, as well as a function that uses other functions as
# helpers.


def get_date(ticket: str) -> str:
    """Return the date of ticket 'ticket' in YYYYMMDD format.

    >>> get_date('20230915YYZYEG12F')
    '20230915'
    >>> get_date('20240915YYZYEG12F1236')
    '20240915'
    """

    return get_year(ticket) + get_month(ticket) + get_day(ticket)

# We provide this function solution as an example of correct function
# documentation, as well as a function that uses constants.


def get_year(ticket: str) -> str:
    """Return the year of ticket 'ticket'.

    >>> get_year('20230915YYZYEG12F')
    '2023'
    >>> get_year('20240915YYZYEG12F1236')
    '2024'
    """

    return ticket[YR:YR + 4]


# We provide the docstring for this function to help you get started.


def get_month(ticket: str) -> str:
    """Return the month of ticket 'ticket'.

    >>> get_month('20230915YYZYEG12F')
    '09'
    >>> get_month('20241215YYZYEG12F1236')
    '12'
    """

    return ticket[MON:MON + 2]


def get_day(ticket: str) -> str:
    """Return the day of ticket 'ticket'.

    >>> get_day('20230915YYZYEG12F')
    '15'
    >>> get_day('20231221YYZYEG25F4442')
    '21'
    """

    return ticket[DAY:DAY + 2]


def get_departure(ticket: str) -> str:
    """Return the departure airport code of ticket 'ticket'.

    >>> get_departure('20231221YYZYEG25F4442')
    'YYZ'
    >>> get_departure('20231221YEGYYZ25F4442')
    'YEG'
    """

    return ticket[DEP:DEP + 3]


def get_arrival(ticket: str) -> str:
    """Return the arrival airport code of ticket 'ticket'.

    >>> get_arrival('20231221YYZYEG25F4442')
    'YEG'
    >>> get_arrival('20231221YEGYYZ25F4442')
    'YYZ'
    """

    return ticket[ARR:ARR + 3]


def get_row(ticket: str) -> int:
    """Return the row number on the given ticket 'ticket'.

    >>> get_row('20231221YYZYEG25F4442')
    25
    >>> get_row('20231221YEGYYZ24F4442')
    24
    """

    return int(ticket[ROW:ROW + 2])


def get_seat(ticket: str) -> str:
    """Return the seat of ticket 'ticket'.

    >>> get_seat('20230915YYZYEG12F')
    'F'
    >>> get_seat('20241215YYZYEG12A1236')
    'A'
    """

    return ticket[SEAT]


def get_ffn(ticket: str) -> str:
    """Return the frequent flyer number on the given ticket 'ticket'.

    >>> get_ffn('20231221YYZYEG25F')
    ''
    >>> get_ffn('20231221YYZYEG25F4442')
    '4442'
    """

    return ticket[FFN:]


# We provide the docstring for this function to help you get started.


def is_valid_seat(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if this ticket has a valid seat. That is,
    if the seat row is between 'first_row' and 'last_row', inclusive,
    and the seat is SA, SB, SC, SD, SE, or SF.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_seat('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_seat('20230915YYZYEG42F1236', 1, 30)
    False
    >>> is_valid_seat('20230915YYZYEG21Q1236', 1, 30)
    False
    """

    return ((get_row(ticket) >= first_row and get_row(ticket) <= last_row)
            and (get_seat(ticket) == SA or get_seat(ticket) == SB
                 or get_seat(ticket) == SC or get_seat(ticket) == SD
                 or get_seat(ticket) == SE or get_seat(ticket) == SF))


def is_valid_ffn(ticket: str) -> bool:
    """Return True if and only if the frequent flyer number of this ticket
    'ticket' is valid.That is if it is a empty string. A valid non-empty
    frequent flyer number must contain exactly four digits, and the sum of the
    first three digits modulo 10 must be the same as the last (fourth) digit.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_ffn('20230915YYZYEG12F')
    True
    >>> is_valid_ffn('20230915YYZYEG42F4442')
    True
    >>> is_valid_ffn('20230915YYZYEG21Q1245')
    False
    >>> is_valid_ffn('20230915YYZYEG21Q123')
    False
    """

    ffn = ticket[17:]
    if ffn == '':
        return True
    if int(ffn) > 999 and int(ffn) < 10000:
        if (int(ffn[0:1]) + int(ffn[1:2]) + int(ffn[2:3])) % 10 == int(ffn[3:]):
            return True
    return False


def is_valid_date(ticket: str) -> bool:
    """Return True if and only if the date of this ticket 'ticket' is valid.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_date('20230915YYZYEG12F')
    True
    >>> is_valid_date('20241229YYZYEG42F4442')
    True
    >>> is_valid_date('20231315YYZYEG21Q1245')
    False
    >>> is_valid_date('20231133YYZYEG21Q1245')
    False
    """

    year = int(get_year(ticket))
    month = int(get_month(ticket))
    day = int(get_day(ticket))

    if year < 0:
        return False
    if 0 < month < 13:
        if (month < 8 and month % 2 == 1) or (month > 7 and month % 2 == 0):
            return 0 < day < 32
        if month != 2:
            return 0 < day < 31
        if year % 4 == 0 and not (year % 200 == 0 and year % 800 != 0):
            return 0 < day < 30
        return 0 < day < 29

    return False


def is_valid_ticket(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if the ticket 'ticket' with first row first_row
    and last row last_row is in valid format and all of the ticket information
    on this ticket is valid'.

    >>> is_valid_ticket('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_ticket('20231315YEGYYZ12F1236' ,1 , 30)
    False
    >>> is_valid_ticket('12320230915YYZYEG12F1ddd', 1, 30)
    False
    >>> is_valid_ticket('12320230915YYZYEG35F4442' , 1 , 30 )
    False
    """

    if is_valid_ticket_format(ticket):
        return (is_valid_seat(ticket, first_row, last_row)
                and is_valid_ffn(ticket) and is_valid_date(ticket)
                and (get_departure(ticket) != get_arrival(ticket)))

    return False


# We provide the docstring for this function to help you get started.

def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if either departure or arrival airport on
    ticket 'ticket' is the same as 'airport'.


    >>> visits_airport('20230915YYZYEG12F1236', 'YEG')
    True
    >>> visits_airport('20230915YEGYYZ12F1236', 'YEG')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'YVR')
    False
    """

    return ticket[DEP:DEP + 3] == airport or ticket[ARR:ARR + 3] == airport


def connecting(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the two flights are connecting: the first
    flight with ticket 'ticket1' arrives in the same airport as the departure
    point of the second flight with ticket 'ticket2', and the two flights are
    on the same dates.

    Precondition: ticket1 and ticket2 are valid tickets.

    >>> connecting('20230915YYZYEG12D1236', '20230915YEGLAS12E1236')
    True
    >>> connecting('20230915YYZYEG12D1236', '20230916YEGLAS12E1236')
    False
    >>> connecting('20230915YEGLAS12D1236', '20230915YEGYYZ12E1236')
    False
    """

    return (get_date(ticket1) == get_date(ticket2)
            and get_arrival(ticket1) == get_departure(ticket2))

# We provide the docstring for this function to help you get started.


def adjacent(ticket1: str, ticket2: str) -> bool:
    """Return True if any only if the seats in tickets 'ticket1' and
    'ticket2' are adjacent (next to each other). Seats across an aisle
    are not considered to be adjacent.

    Precondition: ticket1 and ticket2 are valid tickets.

    >>> adjacent('20230915YYZYEG12D1236', '20230915YYZYEG12E1236')
    True
    >>> adjacent('20230915YYZYEG12B1236', '20230915YYZYEG12A1236')
    True
    >>> adjacent('20230915YYZYEG12C1236', '20230915YYZYEG12D1236')
    False
    >>> adjacent('20230915YYZYEG12A1236', '20230915YYZYEG11B1236')
    False
    """
    seat1 = get_seat(ticket1)
    seat2 = get_seat(ticket2)
    row1 = get_row(ticket1)
    row2 = get_row(ticket2)

    return ((row1 == row2)
            and ((seat1 == SA and seat2 == SB) or (seat1 == SB and seat2 == SA)
                 or (seat1 == SB and seat2 == SC)
                 or (seat1 == SC and seat2 == SB)
                 or (seat1 == SF and seat2 == SE)
                 or (seat1 == SE and seat2 == SF)
                 or (seat1 == SD and seat2 == SE)
                 or (seat1 == SE and seat2 == SD)))


def behind(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats on the two tickets are one
    immediately behind another.
    Precondition: ticket1 and ticket2 are valid tickets.

    >>> behind('20230915YYZYEG12D1236', '20230915YYZYEG13D1236')
    True
    >>> behind('20230915YYZYEG21B1236', '20230915YYZYEG20B1236')
    True
    >>> behind('20230915YYZYEG12C1236', '20230915YYZYEG12D1236')
    False
    >>> behind('20230915YYZYEG12A1236', '20230915YYZYEG11B1236')
    False
    >>> behind('20230915YYZYEG12A1236', '20230915YYZYEG14A1236')
    False
    """
    seat1 = get_seat(ticket1)
    seat2 = get_seat(ticket2)
    row1 = get_row(ticket1)
    row2 = get_row(ticket2)

    return abs(row1 - row2) == 1 and seat1 == seat2


# We provide the docstring for this function to help you get started.


def get_seat_type(ticket: str) -> str:
    """Return WINDOW, AISLE, or MIDDLE depending on the type of seat in
    ticket 'ticket'.

    Precondition: 'ticket' is a valid ticket.

    >>> get_seat_type('20230915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20230915YYZYEG08B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12C1236')
    'aisle'
    """

    seat = get_seat(ticket)
    if seat == SA or seat == SF:
        return WINDOW
    if seat == SB or seat == SE:
        return MIDDLE

    return AISLE


# We provide this function for you to use as a helper.


def is_valid_ticket_format(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format:

    - year is 4 digits
    - months is 2 digits
    - day is 2 digits
    - departure is 3 letters
    - arrival is 3 letters
    - row is 2 digits
    - seat is a characters
    - frequent flyer number is either empty or 4 digits, and
      it is the last record in 'ticket'

    >>> is_valid_ticket_format('20241020YYZYEG12C1236')
    True
    >>> is_valid_ticket_format('20241020YYZYEG12C12361236')
    False
    >>> is_valid_ticket_format('ABC41020YYZYEG12C1236')
    False
    """

    return (FFN == 17
            and (len(ticket) == 17
                 or len(ticket) == 21 and ticket[FFN:FFN + 4].isdigit())
            and ticket[YR:YR + 4].isdigit()
            and ticket[MON:MON + 2].isdigit()
            and ticket[DAY:DAY + 2].isdigit()
            and ticket[DEP:DEP + 3].isalpha()
            and ticket[ARR:ARR + 3].isalpha()
            and ticket[ROW:ROW + 2].isdigit()
            and ticket[SEAT].isalpha())


def change_seat(ticket: str, row_num: str, seat: str) -> str:
    """Return a new ticket that is in the same format as the input ticket
    'ticket', has the same departure, arrival, date, and frequent flyer number
    as the input ticket, and has a new seat information with the given row
    'row_num' and seat 'seat'.

    Precondition: 'ticket and the new seat information are valid'.

    >>> change_seat('20241020YYZYEG12C1236' , '14' , 'D')
    '20241020YYZYEG14D1236'
    >>> change_seat('20230915YYZYEG12F1236' , '25' , 'B')
    '20230915YYZYEG25B1236'
    """

    if ROW < SEAT:
        return (ticket[:ROW] + row_num + ticket[ROW + 2:SEAT]
                + seat + ticket[SEAT + 1:])

    return (ticket[:SEAT] + seat + ticket[SEAT + 1:ROW]
            + row_num + ticket[ROW + 2:])


def change_date(ticket: str, day: str, month: str, year: str) -> str:
    """Return a new ticket that is in the same format as the input ticket
    'ticket', has the same departure, arrival, seat information, and frequent
    flyer number as the input ticket, and has a new date with day 'day' , month
    'month' and year 'year'.

    Precondition:'assume the ticket and the new date information are valid.'


    >>> change_date('20241020YYZYEG12C1236' , '14' , '02' , '2023')
    '20230214YYZYEG12C1236'
    >>> change_date('20230915YYZYEG12F1236' , '31' , '11' , '2026')
    '20261131YYZYEG12F1236'
    """

    return (ticket[:YR] + year + ticket[YR + 4:MON] + month
            + ticket[MON + 2:DAY] + day + ticket[DAY + 2:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
