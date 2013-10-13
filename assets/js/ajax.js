$(function()){
	$('#search').keyup(function() { /*event handler*/

		$.ajax({
			type: "POST",
			url: "/articles/search/",
			data: {
				'search_text':$('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()

			},
			sucess: searchSuccess,
			dataType: 'html'
		});
 	});
});

function searchSucess(data, textStatus, jqXHR)
{
	$('#search-results').html(date)
}

