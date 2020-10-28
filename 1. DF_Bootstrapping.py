"""
The daily BBSW market yield has a dozens of term points, but the calculation of market value of a banking book requires monthly discount factors up to 30 years (360 months). 
So, the first step is uploading the market yield and generate the daily monthly discount factors.

Input: Market Yield Curve (BBSW + Swap Markets Rate)
Output: 
"""

