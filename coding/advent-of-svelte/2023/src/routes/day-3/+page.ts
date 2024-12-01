import type { PageLoad } from './$types';

export interface Child {
	name: string;
	weight: number;
}

export const load: PageLoad = async ({ fetch }) => {
	try {
		const response = await fetch('https://advent.sveltesociety.dev/data/2023/day-three.json');

		const initialData = (await response.json()) as Child[];

		return { initialData };
	} catch (error) {
		console.error(error);
		return { initialData: [] };
	}
};
