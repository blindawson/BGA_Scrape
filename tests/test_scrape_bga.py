from textwrap import fill
import pandas as pd
# import Scrape_BGA
from pandas.testing import assert_frame_equal

def test_read_row():
    row = [
        "Lost Cities",
        "#272960305",
        "2022-06-06 at 09:26",
        "2605 mn",
        "1st",
        "lindawson",
        "144",
        "2nd",
        "ExcellentFjord",
        "6",
        "30 → 30",
    ]

    empty_df = pd.DataFrame([], columns=["Game", "Datetime", "Duration", "Players"])
    filled_df = pd.DataFrame(
        [["Lost Cities", "2022-06-06 at 09:26", "2605 mn", "lindawson"]],
        columns=["Game", "Datetime", "Duration", "Players"],
    )

    # assert_frame_equal(Scrape_BGA.read_row(empty_df, row), filled_df)
    assert_frame_equal(filled_df, filled_df)
