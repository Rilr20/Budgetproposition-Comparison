<script lang="ts">
    import { onMount } from 'svelte';
    import year_2026 from '../json/new_2026_budget_minimized.json';
    import year_2025 from '../json/new_2025_budget_minimized.json';
    import year_2024 from '../json/new_2024_budget_minimized.json';
    import year_2023 from '../json/new_2023_budget_minimized.json';
    import year_2022 from '../json/new_2022_budget_minimized.json';
    import year_2021 from '../json/new_2021_budget_minimized.json';
    import Table from './table.svelte';

    const options = [2021, 2022, 2023, 2024, 2025, 2026];
    const max = 2;

    let selectedOptions = [2025, 2026];
    $: {
    }
    function findYear(year: number) {
        switch (year) {
            case 2026: 
                return year_2026
            case 2025:
                return year_2025
            case 2024:
                return year_2024
            case 2023:
                return year_2023
            case 2022:
                return year_2022
            case 2021:
                return year_2021
            default:
                return [];
        }
    }
    function buttonPress(e: any) {
        if (selectedOptions.length > max) {
            let year = e.target.value;
            let years = selectedOptions.filter((y) => y != year);
            let year1 = years[0];

            let year2 = years[1];
            let year1_delta = Math.abs(year1 - year);
            let year2_delta = Math.abs(year2 - year);
            let tmp;

            if (year1_delta > year2_delta) {
                tmp = selectedOptions.filter((y) => y != year2);
            } else if (year2_delta > year1_delta) {
                tmp = selectedOptions.filter((y) => y != year1);
            } else {
                tmp = selectedOptions.filter((y) => y != Math.max(year1, year2));
            }
            selectedOptions = [...tmp];
        }
    }
</script>

<div class="container">
    <fieldset class="year-selection">
        <legend>Select Year</legend>
        {#each options as option, index}
            <input
                type="checkbox"
                bind:group={selectedOptions}
                name="options"
                value={option}
                id="option{index}"
                on:change={(e) => buttonPress(e)}
            />
            <label for="option{index}">{option}</label>
        {/each}
    </fieldset>
    <article class="overflow-auto table-article">
        {#if selectedOptions.length == 2}
             <Table new_year={findYear(selectedOptions.sort((a, b) => a-b)[1])} old_year={findYear(selectedOptions.sort((a, b) => a-b)[0])} />
        {:else if selectedOptions.length < 2}
            <Table new_year={{name: "", value:0,child:[]}} old_year={{name: "", value:0,child:[]}} />
        {/if}
                 
    </article>
</div>
