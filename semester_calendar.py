import calendar
import doctest

def semester_calendar(output_type, year, first_month, last_month):
    """
    Returns calendar of year from months first_month to last_month
    in output_type format
    (str, int, int, int) -> (str)
    >>> semester_calendar("html", 2021, 10, 10)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" \
class="month">October 2021</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th \
class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th \
class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td \
class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td \
class="sat">2</td><td class="sun">3</td></tr>\\n<tr><td class="mon">4</td><td \
class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td \
class="sat">9</td><td class="sun">10</td></tr>\\n<tr><td class="mon">11</td><td \
class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td \
class="sat">16</td><td class="sun">17</td></tr>\\n<tr><td class="mon">18</td><td \
class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td \
class="sat">23</td><td class="sun">24</td></tr>\\n<tr><td class="mon">25</td><td \
class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td \
class="fri">29</td><td class="sat">30</td><td class="sun">31</td></tr>\\n</table>\\n'
    >>> semester_calendar("txt", 2022, 11, 11)
    '   November 2022\\nMo Tu We Th Fr Sa Su\\n    \
1  2  3  4  5  6\\n 7  8  9 10 11 12 13\\n\
14 15 16 17 18 19 20\\n21 22 23 24 25 26 27\\n28 29 30\\n'
    """
    result_calendar = ""
    text_calendar = calendar.TextCalendar(firstweekday=0)
    html_calendar = calendar.HTMLCalendar(firstweekday=0)
    if (isinstance(output_type, str)
        and isinstance(year, int)
        and isinstance(first_month, int)
        and isinstance(last_month, int)):
        if output_type == "txt":
            for i in range(first_month, last_month + 1):
                result_calendar += text_calendar.formatmonth(year, i)
            return result_calendar
        if output_type == "html":
            for i in range(first_month, last_month + 1):
                result_calendar += html_calendar.formatmonth(year, i)
            return result_calendar
        return None
    return None

print(doctest.testmod())

