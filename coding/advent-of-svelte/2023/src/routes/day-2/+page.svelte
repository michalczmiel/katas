<script lang="ts">
	const max = 100;
	const min = 0;
	const initial = 0;

	let count = $state(initial);

	const canAdd = $derived(count < max);
	const canRemove = $derived(count > min);
	const canReset = $derived(count !== min);

	function onAdd(): void {
		if (canAdd) {
			count += 1;
		}
	}

	function onRemove(): void {
		if (canRemove) {
			count -= 1;
		}
	}

	function onReset(): void {
		if (canReset) {
			count = min;
		}
	}
</script>

<main>
	<h1>Cookie counter</h1>

	<p>{count}</p>

	<section>
		<button disabled={!canAdd} onclick={onAdd}>Add</button>
		<button disabled={!canRemove} onclick={onRemove}>Remove</button>
		<button disabled={!canReset} onclick={onReset}>Reset</button>
	</section>

	<div>
		<h2>Santa's mood</h2>
		<progress {max} value={count}></progress>
	</div>
</main>

<style>
	button {
		cursor: pointer;
	}
</style>
