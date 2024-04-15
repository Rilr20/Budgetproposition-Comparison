<script lang="ts">
    import { onMount } from 'svelte';
    import Table from './table.svelte';

    $: first_year = { child: [], name: '', id: 0 };
    $: second_year = { child: [], name: '', id: 0 };
    let years = [2021, 2022, 2023, 2024];
    let selected: number[] = [2023, 2024];
    let checked: any = {};
    const max = 2;
    //read files
    // fetch("../../../data-extraction/json/budget.json")
    //     .then(data => data.json())
    onMount(() => {
        async function load() {
            const response = await fetch(
                'src/json/revision_budgetpropositionen-for-' + selected[0] + '.json'
            );
            const response2 = await fetch(
                'src/json/revision_budgetpropositionen-for-' + selected[1] + '.json'
            );
            const data = await response.json();
            const data2 = await response2.json();
            first_year = data;
            second_year = data2;
            // console.log(first_year);
            // console.log(second_year);
            // return data
        }
        load();
    });

    function handleInput(event: any) {
        const value = event.target.value;
        if (event.target.checked) {
            if (selected.length === max) {
                const last: any = selected.pop();
                delete checked[last];
            }
            selected.push(value);
        } else {
            selected = selected.filter((options) => options !== value);
        }
    }
</script>

<fieldset>
    <legend>Select Year</legend>
    {#each years as year}
        <input
            type="checkbox"
            on:input={handleInput}
            value={year}
            id={year.toString()}
            name={year.toString()}
            bind:checked={checked[year]}
        />
        <label for={year.toString()}>{year}</label>
    {/each}
</fieldset>
<!-- <progress class="pico-background-pink-500" /> -->
<Table
    old_year_children={first_year.child}
    new_year_children={second_year.child}
    old_year={selected[0]}
    new_year={selected[1]}
/>
