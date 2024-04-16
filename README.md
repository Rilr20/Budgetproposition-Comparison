<!-- # Budgetproposition Comparison -->
<!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


## Budgetpropositionen PDF
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

* 2021 https://www.regeringen.se/rattsliga-dokument/proposition/2020/09/prop.-2020211
* 2022 https://www.regeringen.se/rattsliga-dokument/proposition/2021/09/prop.-2021221
* 2023 https://www.regeringen.se/rattsliga-dokument/proposition/2022/11/prop.-2022231
* 2024 https://www.regeringen.se/rattsliga-dokument/proposition/2023/09/prop.-2023241

## SCB data
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-konsumtion/konsumentprisindex/konsumentprisindex-kpi/pong/tabell-och-diagram/konsumentprisindex-kpi/kpi-faststallda-tal-1980100/ -->

# Budgetproposition Comparison

## Description

This project aims to compare the budget propositions of each year to identify the percentage increase and decrease in expenditure areas. It also has the potential to include income areas and display them, though this feature is not implemented.

## Current Status

This project was just made for fun where I applied technologies I'm familiar with and learn more about. 

## Requirements

- Python for data extraction
- TypeScript and Svelte for data display

## Technologies Used

- Python
- TypeScript
- Svelte

## Data Sources

### Budgetproposition
Budgetpropositionen from [Regeringen](https://regeringen.se/) that has been tested on.
* 2021 https://www.regeringen.se/rattsliga-dokument/proposition/2020/09/prop.-2020211
* 2022 https://www.regeringen.se/rattsliga-dokument/proposition/2021/09/prop.-2021221
* 2023 https://www.regeringen.se/rattsliga-dokument/proposition/2022/11/prop.-2022231
* 2024 https://www.regeringen.se/rattsliga-dokument/proposition/2023/09/prop.-2023241


<!-- - Budget propositions: Data from [riksdagen.se](https://riksdagen.se) -->
### Konsumentproduktindex
Inflation data from [SCB](https://www.scb.se)
- [Konsumentprisindex (KPI)](https://www.scb.se/hitta-statistik/statistik-efter-amne/priser-och-konsumtion/konsumentprisindex/konsumentprisindex-kpi/pong/tabell-och-diagram/konsumentprisindex-kpi/kpi-faststallda-tal-1980100/) 

## Known Issues

- Potential regex edge cases that may appear in untested budget propositions.

- Challenges in handling changes in naming conventions for the different budget propositions, one example being when comparing 2021 and 2022 (to 2024) "2 Riksdagen och dess myndigheter" and "2 Riksdagen samt Riksdagens ombudsmän", should logically be considered the same but are treated as separate entities due to the change in naming.

## Future Enhancements

- The possibility to include income areas and display them, as the data is available but not currently used or extracted.