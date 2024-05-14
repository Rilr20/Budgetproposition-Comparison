<script lang="ts">
    import Pagination from './pagination.svelte';

    export let old_year: number;
    export let new_year: number;
    export let old_year_children: any;
    export let new_year_children: any;

    let old_year_slice: any;
    let new_year_slice: any;
    console.log(new_year_slice + ' asd');

    export let id = '';
    let value_array: Record<string, string> = [];
    function percentageIncrease(a: number, b: number): number {
        return parseFloat((((b - a) / a) * 100).toFixed(2));
    }
    function percentageColor(percentage: number): string {
        if (Math.floor(percentage) === 0) {
            return 'pico-color-slate-200';
        } else if (percentage > 0 && percentage < 10) {
            return 'pico-color-jade-50';
        } else if (percentage < 0 && percentage > -10) {
            return 'pico-color-pink-50';
        } else if (percentage <= -85) {
            return 'pico-color-pink-450';
        } else if (percentage <= -50) {
            return 'pico-color-pink-350';
        } else if (percentage <= -30) {
            return 'pico-color-pink-250';
        } else if (percentage <= -20) {
            return 'pico-color-pink-200';
        } else if (percentage <= -10) {
            return 'pico-color-pink-150';
        } else if (percentage >= 10000) {
            return 'pico-color-jade-450';
        } else if (percentage >= 1000) {
            return 'pico-color-jade-350';
        } else if (percentage >= 200) {
            return 'pico-color-jade2500';
        } else if (percentage >= 50) {
            return 'pico-color-jade-200';
        } else if (percentage >= 10) {
            return 'pico-color-jade-150';
        }
        return 'pico-color-orange-900';
    }

    function calculateInflation(old_year: number, new_year: number): number {
        let KPI_per_year: Record<number, number> = {
            // 2024: 414.26, //month of march
            2023: 403.7,
            2022: 371.91,
            2021: 343.19,
            2020: 335.92,
            2019: 334.26,
            2018: 328.4,
            2017: 322.11,
            2016: 316.43,
            2015: 313.35,
            2014: 313.49,
            2013: 314.06,
            2012: 314.2,
            2011: 311.43,
            2010: 303.46,
            2009: 299.66,
            2008: 300.61,
            2007: 290.51
        };

        // minus one because the budget proposition is created during november the previous year
        let years = [old_year - 1, new_year - 1].sort((a, b) => {
            return b - a;
        });

        let old_year_KPI = KPI_per_year[years[0]];
        let new_year_KPI = KPI_per_year[years[1]];

        let result = ((old_year_KPI - new_year_KPI) / new_year_KPI) * 100;

        return parseFloat(result.toFixed(4));
    }
    function stringToNum(inputString: string) {
        return parseFloat(inputString.replaceAll(' ', ''));
    }
    function findSubstring(substr: string, jsonData: any) {
        return jsonData.some((item) => {
            return (
                item.name.substring(item.name.indexOf(' ') + 1).length == substr.length &&
                item.name.toLowerCase().includes(substr.toLowerCase())
            );
        });
    }
    function findSameExpenditure(
        inputString: string,
        jsonData,
        value_index: number,
        inputExpenditure: string
    ): string {
        let next_return = { value: '' };

        let item = jsonData.find((item) => {
            if (
                item.name.toLowerCase().includes(inputString.toLowerCase()) &&
                item.name.substring(item.name.indexOf(' ') + 1).length == inputString.length
            ) {
                if (
                    percentageIncrease(stringToNum(inputExpenditure), stringToNum(item.value)) > 400
                ) {
                    let foundData = [];
                    for (let i = 0; i < jsonData.length; i++) {
                        if (
                            jsonData[i].name.toLowerCase().includes(inputString.toLowerCase()) &&
                            jsonData[i].name.substring(jsonData[i].name.indexOf(' ') + 1).length ==
                                inputString.length
                        ) {
                            foundData.push(jsonData[i]);
                            next_return = jsonData[i];
                        }
                    }
                    if (foundData.length === 1) {
                        next_return = foundData[0];
                    }
                    if (foundData.length === 3) {
                        foundData.sort(
                            (a, b) =>
                                Math.abs(stringToNum(a.value) - stringToNum(inputExpenditure)) -
                                Math.abs(stringToNum(b.value) - stringToNum(inputExpenditure))
                        );
                        next_return = foundData[0];
                    } else {
                        foundData.forEach((item) => {
                            if (
                                percentageIncrease(
                                    stringToNum(inputExpenditure),
                                    stringToNum(item.value)
                                ) < 500
                            ) {
                                next_return = item;
                            }
                        });
                    }
                    value_array[value_index] = next_return.value;
                    return next_return;
                } else {
                    value_array[value_index] = item.value;
                    return item;
                }
            }
        });
        return next_return.value == '' ? item.value : next_return.value;
    }
</script>

<article style="overflow-x:auto;">
    <p>* Thousands of sek</p>
    <table class="striped" data-theme="dark">
        <tr>
            <th>Expenditure area</th>
            <th>{old_year}</th>
            <th>{new_year}</th>
            <th>%</th>
            <th>% inflation</th>
        </tr>
        {#if old_year_slice}
            {#each old_year_slice as item, index}
                {#if new_year_slice[index] !== undefined}
                    {#if !findSubstring(new_year_slice[index].name.substring(new_year_slice[index].name.indexOf(' ') + 1), old_year_slice)}
                        <tr>
                            <td>{new_year_slice[index].name}</td>
                            <td>N/A</td>
                            <td>{new_year_slice[index].value.replaceAll(' ', '.')}</td>
                            <td>N/A</td>
                            <td>N/A</td>
                        </tr>
                    {/if}
                    {#if !findSubstring(item.name.substring(item.name.indexOf(' ') + 1), new_year_slice)}
                        <tr>
                            <td>{item.name}</td>
                            <td>{item.value.replaceAll(' ', '.')}</td>
                            <td>N/A</td>
                            <td>N/A</td>
                            <td>N/A</td>
                        </tr>
                    {:else}
                        <tr>
                            {#if item.is_bold}
                                <td style="font-weight: bold">{item.name}</td>
                            {:else}
                                <td>{item.name}</td>
                            {/if}
                            <td>{item.value.replaceAll(' ', '.')}</td>
                            <td
                                >{findSameExpenditure(
                                    item.name.substring(item.name.indexOf(' ') + 1),
                                    new_year_children,
                                    index,
                                    item.value
                                ).replaceAll(' ', '.')}</td
                            >
                            <td
                                class={percentageColor(
                                    percentageIncrease(
                                        stringToNum(item.value),
                                        stringToNum(value_array[index])
                                    )
                                )}
                            >
                                {percentageIncrease(
                                    stringToNum(item.value),
                                    stringToNum(value_array[index])
                                )}%
                            </td>
                            <td
                                class={percentageColor(
                                    percentageIncrease(
                                        stringToNum(item.value) +
                                            (stringToNum(item.value) / 100) *
                                                calculateInflation(old_year, new_year),
                                        stringToNum(value_array[index])
                                    )
                                )}
                            >
                                {percentageIncrease(
                                    stringToNum(item.value) +
                                        (stringToNum(item.value) / 100) *
                                            calculateInflation(old_year, new_year),
                                    stringToNum(value_array[index])
                                )}%
                            </td>
                        </tr>
                    {/if}
                {/if}
            {/each}
        {/if}
    </table>
</article>
