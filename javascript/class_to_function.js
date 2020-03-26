// código da vídeo aula do canal DevPleno https://www.youtube.com/watch?v=po9Ik_v5koU
/*class Calc {
	constructor(num1, num2){
		this.num1 = num1
		this.num2 = num2
	}
	
	out(){
		console.log(this.num1, this.num2)
	}
}

const a = new Calc(1,2)
a.out.bind({num1: 4, num2:5})()
*/

const Calc = function(num1, num2){
	const soma = num1 + num2
	return {
		//arrow function não sobreescreve this
		out: () => {
			console.log(num1, num2, soma)
		}
	}
}

const a = new Calc(1,2)
a.out()
a.out.bind({num1: 4, num2:5})()