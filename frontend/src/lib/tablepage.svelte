<script lang="ts">
    import { onMount } from 'svelte';
    import Table from './table.svelte';
    import year_2025 from '../json/budget-2025.json';
    import year_2024 from '../json/budget-2024.json';
    import year_2023 from '../json/budget-2023.json';
    import year_2022 from '../json/budget-2022.json';
    import year_2021 from '../json/budget-2021.json';

    // $: first_year = { child: [], name: '', id: 0 };
    // $: second_year = { child: [], name: '', id: 0 };
    // let years = [];
    const options = [2021, 2022, 2023, 2024, 2025];
    const max = 2;

    let selectedOptions = [2024, 2025];
    $: {

    }
    function findYear(year: number) {
        switch (year) {
            case 2025:
                return year_2025.child;
            case 2024:
                return year_2024.child;
            case 2023:
                return year_2023.child;
            case 2022:
                return year_2022.child;
            case 2021:
                return year_2021.child;
            default:
                return []
        }
    }
</script>
<article>

    <fieldset>
        <legend>Select Year</legend>
        {#each options as option, index}
        <!-- <div class="option"> -->
            <input
        type="checkbox"
        bind:group={selectedOptions}
        name="options"
        value={option}
        id="option{index}"
        disabled={selectedOptions.length === max && !selectedOptions.includes(option)}
        />
        <label for="option{index}">{option}</label>
    <!-- </div> -->
    {/each}
</fieldset>

<Table
    old_year_children={findYear(selectedOptions.sort((a, b) => a-b)[0])}
    new_year_children={findYear(selectedOptions.sort((a, b) => a-b)[1])}
    old_year={selectedOptions.sort((a, b) => a-b)[0] == undefined ? 0 : selectedOptions.sort((a,b) => a-b)[0]}
    new_year={selectedOptions.sort((a, b) => a-b)[1] == undefined ? 0 : selectedOptions.sort((a,b) => a-b)[1]}
    />
    
</article>