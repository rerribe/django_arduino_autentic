console.log('teste do console')

const troca_valor = document.getElementById('cartao');
console.log(troca_valor.value)

const btn = document.querySelector("button");

btn.addEventListener("click", function() {

	$.ajax({
		type:'GET',
		url: 'resposta_arduino',
		success: function(response){
			troca_valor.value = response.chave
			alert(response.chave)
			console.log('ae, mto bem')
		},
	});	
});



