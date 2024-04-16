<script lang="ts">
    export let old_year: number;
    export let new_year: number;
    export let old_year_children: any;
    export let new_year_children: any;
    // console.log(new_year_children);

    export let id = '';
    let value_array: Record<string, string> = [];
    function percentage_increase(a: number, b: number): number {
        // let abs = Math.abs(a - b)
        // let avg = (a+b) / 2
        // return (100 * (Math.abs(a - b)) / ((a+b) / 2)).toFixed(2)
        return parseFloat((((b - a) / a) * 100).toFixed(2));
    }
    function color_on_percentage(percentage: number): string {
        // console.log(percentage);

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

    function calculate_inflation(old_year: number, new_year: number): number {
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
    function string_to_num(inputString: string) {
        return parseFloat(inputString.replaceAll(' ', ''));
    }
    function search_for_substring(substr: string, jsonData: any) {
        return jsonData.some((item) => {
            return (
                item.name.substring(item.name.indexOf(' ') + 1).length == substr.length &&
                item.name.toLowerCase().includes(substr.toLowerCase())
            );
        });
    }
    function find_same_expenditure(inputString: string, jsonData, value_index: number): string {
        let item = jsonData.find((item) => {
            if (
                item.name.substring(item.name.indexOf(' ') + 1).length == inputString.length &&
                item.name.toLowerCase().includes(inputString.toLowerCase())
            ) {
                value_array[value_index] = item.value;

                return item;
            }
        });
        return item.value;
    }
</script>

<article style="margin-top: 1em">
    <p style="text-align: right; margin-right:0.5em;">* Thousands of sek</p>
    <table data-theme="dark">
        <tr>
            <th>Expenditure area</th>
            <th>{old_year}</th>
            <th>{new_year}</th>
            <th>%</th>
            <th>% inflation</th>
        </tr>

        {#each old_year_children as item, index}
            {#if new_year_children[index] !== undefined}
                {#if !search_for_substring(new_year_children[index].name.substring(new_year_children[index].name.indexOf(' ') + 1), old_year_children)}
                    <tr>
                        <td>{new_year_children[index].name}</td>
                        <td>N/A</td>
                        <td>{new_year_children[index].value.replaceAll(' ', '.')}</td>
                        <td>N/A</td>
                        <td>N/A</td>
                    </tr>
                {/if}
                {#if !search_for_substring(item.name.substring(item.name.indexOf(' ') + 1), new_year_children)}
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
                            >{find_same_expenditure(
                                item.name.substring(item.name.indexOf(' ') + 1),
                                new_year_children,
                                index
                            ).replaceAll(' ', '.')}</td
                        >
                        <td
                            class={color_on_percentage(
                                percentage_increase(
                                    string_to_num(item.value),
                                    string_to_num(value_array[index])
                                )
                            )}
                        >
                            {percentage_increase(
                                string_to_num(item.value),
                                string_to_num(value_array[index])
                            )}%
                        </td>
                        <td
                            class={color_on_percentage(
                                percentage_increase(
                                    string_to_num(item.value) +
                                        (string_to_num(item.value) / 100) *
                                            calculate_inflation(old_year, new_year),
                                    string_to_num(value_array[index])
                                )
                            )}
                        >
                            {percentage_increase(
                                string_to_num(item.value) +
                                    (string_to_num(item.value) / 100) *
                                        calculate_inflation(old_year, new_year),
                                string_to_num(value_array[index])
                            )}%
                        </td>
                    </tr>
                {/if}
            {/if}
        {/each}
    </table>
</article>
