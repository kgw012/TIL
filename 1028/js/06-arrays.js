/*
	[배열 관련 주요 메서드 연습 1]
	
	주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만드세요.
*/

const homeworks = ['david.zip', null, 'maria.zip', 'tom.zip', null]

const result = []
for (let homework of homeworks) {
	if (homework != null) {
		result.push(homework)
	}
}

console.log(result)
// ['david.zip', 'maria.zip', 'tom.zip']


/*
	[배열 관련 주요 메서드 연습 2]
	
	주어진 배열을 사용하여 아래 문자열을 완성하세요.

	'www.samsung.com/sec/buds/galaxy-buds-pro'

*/

const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']

const str1 = arr1.join('.')
const str2 = arr2.join('-')
const str3 = arr3.join('/')

const strs = [str1, str3, str2]
const result = strs.join('/')

console.log(result)
// www.samsung.com/sec/buds/galaxy-buds-pro


/*
	[배열 관련 주요 메서드 연습 3]

	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']

let i = weather.indexOf('rainy')
while (i >= 0) {
	weather[i] = 'sunny'
	i = weather.indexOf('rainy')
}

console.log(weather)
// ['sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny']
