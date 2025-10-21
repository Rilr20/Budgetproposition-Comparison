<script lang="ts">
    import {createEventDispatcher, tick} from "svelte"
    export let child: {
        new_year_value: string | null;
        old_year_value: string | null;
        name: string;
        value: number;
        child: [];
    };
    export let visible: boolean;
    // export let new_year: any;
    export let structure: string[];
    const new_year = 2025;
    const old_year = 2024;
    let child_visibility = false;
    $: trueVisibility = visible && child_visibility;
    const dispatch = createEventDispatcher()
    function changeVisible() {
        child_visibility = !child_visibility;
        dispatch('visibilityChange')
    }
    // $: dispatch("visibilityChange", trueVisibility)

    function percentageIncrease(aI: string | null, bI: string | null): number {

        if (aI == null || bI == null) {
            return 0;
        }
        let a = stringToNum(aI);
        let b = stringToNum(bI);

        return parseFloat((((b - a) / a) * 100).toFixed(2));
    }
    function percentageColour(percentage: number): string {
        const darkmode = false;
        if (darkmode) {
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
                return 'pico-color-jade-250';
            } else if (percentage >= 50) {
                return 'pico-color-jade-200';
            } else if (percentage >= 10) {
                return 'pico-color-jade-150';
            }
        } else {
            if (Math.floor(percentage) === 0) {
                return 'pico-color-slate-450';
            } else if (percentage > 0 && percentage < 10) {
                return 'pico-color-jade-350';
            } else if (percentage < 0 && percentage > -10) {
                return 'pico-color-pink-350';
            } else if (percentage <= -85) {
                return 'pico-color-pink-700';
            } else if (percentage <= -50) {
                return 'pico-color-pink-600';
            } else if (percentage <= -30) {
                return 'pico-color-pink-500';
            } else if (percentage <= -20) {
                return 'pico-color-pink-450';
            } else if (percentage <= -10) {
                return 'pico-color-pink-400';
            } else if (percentage >= 10000) {
                return 'pico-color-jade-700';
            } else if (percentage >= 1000) {
                return 'pico-color-jade-600';
            } else if (percentage >= 200) {
                return 'pico-color-jade-500';
            } else if (percentage >= 50) {
                return 'pico-color-jade-450';
            } else if (percentage >= 10) {
                return 'pico-color-jade-400';
            }
        }

        return 'pico-color-orange-900';
    }

    function calculateInflation(old_year: number, new_year: number): number {
        let KPI_per_year: Record<number, number> = {
            2025: 418.13, //month of august
            2024: 415.15,
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
    function stringToNum(inputString: string): number {
        return parseFloat(inputString.replaceAll(' ', ''));
    }

    function precalcInflation(
        old_year_value: string,
        start_year: number,
        end_year: number
    ): string {
        let a = stringToNum(old_year_value);

        let res = (a / 100) * calculateInflation(start_year, end_year);
        return (a + res).toString();
    }
    const percentage = percentageIncrease(child.old_year_value, child.new_year_value);
    let percentageInflationAdj: string | number = '';
    let percentageInflationAdjCol;
    if (child.old_year_value) {
        percentageInflationAdj = percentageIncrease(
            precalcInflation(child.old_year_value, old_year, new_year),
            child.new_year_value
        );
        percentageInflationAdjCol = percentageColour(percentageInflationAdj);
    }
    const percentageCol = percentageColour(percentage);

    function splitName() {
        
        let newStruct = structure.slice(1, structure.length)
        if (newStruct.length > 0) {
            let res = newStruct.map((item) => {
                return item.split(" ")[0]
            })
            let string = "&nbsp;".repeat(newStruct.length)
            
            string += res.join(".")+"."
            
            return string

        }
        return ""
    }
</script>

<tr class="table-row" style="display: {visible ? 'table-row' : 'none'}">
    <td style="">
        {#if child.name.includes('BOLD')}
            <b>{@html splitName()}{child.name.split('BOLD')[0]} {child.name.split('BOLD')[1]}</b>
        {:else}
            {@html splitName()}{child.name}
        {/if}
    </td>
    <td style="text-align: right; white-space: nowrap;" class="value"
        >{child.old_year_value != null ? `${child.old_year_value} tkr` : ''}</td
    >
    <td style="text-align: right; white-space: nowrap;" class="value"
        >{child.new_year_value != null ? `${child.new_year_value} tkr` : ''}</td
    >
    <!-- {#if new_year}
        <td style="text-align: right; white-space: nowrap;" class="value"
            >{createData(new_year, child.name, structure)}</td
        >
    {:else}
        <td></td>
    {/if} -->
    <td class={percentageCol}>{percentage}%</td>
    <td class={percentageInflationAdjCol}>
        {percentageInflationAdj}%
    </td>

    {#if child.child.length != 0}
        <td>
            <div style="width:auto;height:auto;" class="arrow-container">
                <div
                    class={!child_visibility ? 'arrow' : 'arrow-opposite'}
                    on:click={() => changeVisible()}
                ></div>
            </div>
        </td>
    {:else}
        <td></td>
    {/if}
</tr>
{#if child.child != undefined}
    {#each child.child as grandchild, index}
        <svelte:self
            structure={[...structure, child.name]}
            child={grandchild}
            visible={trueVisibility}
            on:visibilityChange={(e) => dispatch("visibilityChange", e.detail)}
        ></svelte:self>
    {/each}
{/if}
