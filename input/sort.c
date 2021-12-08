#include <stdlib.h>
#include <stdio.h>

void sort(int* arr, int n) {
	int i, j, change = 0;
	for (i = n - 1; i >= 0; i--) {
		for (j = 0; j < i; j++) {
			if (arr[j] > arr[j + 1]) {
				arr[j] = arr[j + 1] + arr[j];
				arr[j + 1] = arr[j] - arr[j + 1];
				arr[j] = arr[j] - arr[j + 1];
				change = 1;
			}
		}
		if (change == 0) break;
	}
}

int main() {
	int i, n;
	scanf("%d", &n);
	int* arr = malloc(sizeof(int) * n);
	for (i = 0; i < n; i++) {
		scanf("%d", arr + i);
	}
	sort(arr, n);
	for (i = 0; i < n; i++) {
		printf("%d ", arr[i]);
	}
	printf("\n");
	return 0;
}