/*
 [배열 관련 주요 메서드 연습 심화 1]
 
 속력(distance/time)을 저장하는 배열 speeds를 만드세요.
*/

const trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 },
]

const speeds = trips.map(e => e.distance / e.time)
console.log(speeds)
// [3.4, 1.8, 2.36]


/*
 [배열 관련 주요 메서드 연습 심화 2]
 
 주어진 배열의 요소 중 특정 문자(query)가 포함되는 요소만 모아서 새로운 배열을 반환하세요.
*/

const languages = ['python', 'javascript', 'html', 'java']
const query = 'java'

const result = languages.filter(e => e.includes(query))
console.log(result)
// ['javascript', 'java']


/*
 [배열 관련 주요 메서드 연습 심화 3]
 
 주어진 배열을 사용하여 다음과 같은 객체를 만드세요.
 {
   smith: 90,
   peter: 80,
   anna: 85,
 }
*/

const scores = [
  { name: 'smith', score: 90 },
  { name: 'peter', score: 80 },
  { name: 'anna', score: 85 },
]

// reduce 이용 풀이
const result = scores.reduce((acc, e) => {
  acc[e.name] = e.score
  return acc
}, {})
console.log(result)
// {smith: 90, peter: 80, anna: 85}

// forEach 이용 풀이
const result = {}
scores.forEach(e => result[e.name] = e.score)
console.log(result)
// {smith: 90, peter: 80, anna: 85}


/*
 [배열 관련 주요 메서드 연습 심화 4]
 
 주어진 accounts 배열에서 balance가 24,000인 사람을 찾으세요.
*/

const accounts = [
	{ name: 'justin', balance: 1200 },
	{ name: 'harry', balance: 50000 },
	{ name: 'jason', balance: 24000 },
]

const result = accounts.find(e => e.balance === 24000)
console.log(result)


/*
 [배열 관련 주요 메서드 연습 심화 5]
 
 주어진 requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
*/

const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

const result = requests.some(e => e.status === 'pending')
console.log(result)


/*
 [배열 관련 주요 메서드 연습 심화 6]
 
 주어진 users 배열을 통해 모든 유저의 상태가 submmited인지 여부를 확인하세요.
*/

const users = [
  { username: 'eric', submitted: true },
  { username: 'justin', submitted: true},
  { username: 'james', submitted: false},
]

const result = users.every(e => e.submitted)
console.log(result)
