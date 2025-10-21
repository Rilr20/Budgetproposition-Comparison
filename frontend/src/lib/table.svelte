<script lang="ts">
    import Tabledata from './tabledata.svelte';
    import { onMount, tick } from 'svelte';

    export let old_year: { name: string; child: []; value: number };
    export let new_year: { name: string; child: []; value: number };
    const combinedNodes = combineYears(old_year, new_year);
    function combineYears(oldNode = old_year, newNode = new_year): object {
        let merged = { name: '', value: 0, child: [] };
        let new_txt_arr: string[] = oldNode.name.split(' ');
        let next_year = newNode.name.split(' ');
        new_txt_arr.push('-', next_year[next_year.length - 1]);
        let new_txt = new_txt_arr.join(' ');
        merged.name = new_txt;

        // merged.name = old_year?.name  new_year.?name
        merged.child = combineNodes(old_year?.child ?? [], new_year?.child ?? []);
        return merged;
    }
    function combineNodes(oldNode: any, newNode: any): any {
        const mergedNodes = [];

        const allNames = [
            ...new Set([
                ...oldNode.map((c: { name: string }) => c.name.split(' ').slice(1).join(' ')),
                ...newNode.map((c: { name: string }) => c.name.split(' ').slice(1).join(' '))
            ])
        ];
        for (let name of allNames) {
            // let splitName = name.split(" ")
            // splitName.shift()
            // splitName = splitName.join(" ")

            // let oldMatch = oldNode.find((c: { name: string; }) => c.name.split(" ").shift().join(" ") === splitName)
            let oldMatch = oldNode.find(
                (c: { name: string }) => c.name.split(' ').slice(1).join(' ') === name
            );

            let newMatch = newNode.find(
                (c: { name: string }) => c.name.split(' ').slice(1).join(' ') === name
            );

            const merged = {
                name: oldMatch?.name || newMatch?.name,
                old_year_value: oldMatch?.value ?? null,
                new_year_value: newMatch?.value ?? null,
                child: combineNodes(oldMatch?.child ?? [], newMatch?.child ?? [])
            };
            mergedNodes.push(merged);
        }
        mergedNodes.sort((a, b) => {
            return a.name.split(' ')[0] - b.name.split(' ')[0];
        });

        return mergedNodes;
    }
    function tableRowColours() {
        const tableRows = [...document.getElementsByClassName('table-row')];
        const visibleRows = tableRows.filter((item) => item.style.display === 'table-row');
        visibleRows.forEach((element, idx) => {
            if (idx % 2 == 0) {
                element.classList.add('stripe-1');
                element.classList.remove('stripe-2');
            } else {
                element.classList.remove('stripe-1');
                element.classList.add('stripe-2');
            }
        });
    }
    async function handleVisibilityChange() {
        await tick(); // wait until DOM reflects the new visibility
        tableRowColours();
    }
    onMount(() => {
        tableRowColours();
    });
</script>

<table>
    <tr>
        {#if old_year.name.split(' ')[7] != undefined}
            <th>Utgiftsområde</th>
            <!-- content here -->
            <th style="text-align:right;">{old_year.name.split(' ')[7]}</th>
            <th style="text-align:right;">{new_year.name.split(' ')[7]}</th>
            <th>Procent</th>
            <th>Inflation</th>
            <th> </th>
        {:else}
             <!-- else content here -->
            <th style="width: 696.517px">Utgiftsområde</th>
            <th style="width: 143.95px; text-align:right;">{""}</th>
            <th style="width: 143.95px; text-align:right;">{""}</th>
            <th style="width: 75.4px;">Procent</th>
            <th style="width: 76.183px;">Inflation</th>
            <th style="width: 20px;"> </th>
        {/if}
    </tr>
    {#each combinedNodes.child as child, index}
        <Tabledata
            on:visibilityChange={handleVisibilityChange}
            structure={[old_year.name]}
            {child}
            visible={true}
        ></Tabledata>
    {/each}
</table>
