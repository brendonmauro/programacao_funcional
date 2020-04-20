// codigo referente a aula do canal Dev Pleno
// sobre pure function https://youtu.be/1OrEqycGoiM

// non pure functions

class Test {
	attr = 0
	
	// depende do estado do atributo da classe
	// a saída deveria ser sempre de acordo com a entrada se fosse uma função pura
	public function somar(){
		attr++;
	}
	
	public function subtrair(){
		attr--;
	}
	
}


// Pure functions

function funcaoPuraContaMais(contador){
	return contador + 1
}


funcaoPuraContaMais(-1) == 0
funcaoPuraContaMais(0) == 1
funcaoPuraContaMais(1) == 2
