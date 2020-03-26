// aula do canal do youtube devpleno https://www.youtube.com/watch?v=rec4I8zfYjc

function func1(valor1, valor2){
	return valor1 + valor2
}

console.log('normal', func1(1,2))

function func2(valor1){
	return function(valor2){
		return valor1 + valor2
	}
}

const func2Valor1 = func2(10)

console.log('curried', func2Valor1(20))
console.log('curried', func2(10)(20))

const funcArrow = (valor1) => (valor2) => (valor3) =>  {
	return valor1+valor2+valor3
}

console.log(funcArrow(1)(2)(3))