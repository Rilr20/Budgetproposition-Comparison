<script>
    export let old_year_children
    export let new_year_children
    export let old_year_slice
    export let new_year_slice
    export let perPage=30;

    $: totalRows = old_year_children.length 
    $: currentPage = 0
    $: totalPages = Math.ceil(totalRows / perPage) 
    $: start =  currentPage * perPage
    $: end = currentPage === totalPages - 1 ? totalRows - 1 : start + perPage - 1  ;
    $: old_year_slice = old_year_children.slice(start, end + 1);
    $: new_year_slice = new_year_children.slice(start, end + 1);
    $: totalRows, currentPage = 0
    $: currentPage, start, end
</script>
<div  class="pagination">
    
    <button disabled={currentPage===0} class="pagination-btn" on:click={() => currentPage -=1}>←</button>
    <p class="min-width: 213px" style="text-align: center;">Page {currentPage+1} out of {totalPages}</p>
    <button disabled={currentPage===totalPages-1} class="pagination-bth" on:click={() => currentPage +=1}>→</button>
</div>
