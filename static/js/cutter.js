window.onload = function() 
{	
	var file_input = document.getElementById('file_input');
	file_input.addEventListener('change', function(e) 
	{
				
		var form_data = new FormData($('#upload-file')[0]);
		
		$.ajax({
			type: 'POST',
			url: '/uploadajax',
			data: form_data,
			contentType: false,
			cache: false,
			processData: false,
			async: false,
			success: function(data) 
			{
				d = new Date();
				$('#image_preview object').attr("data", "svg/pattern.svg?"+d.getTime());
			},
		});
	});

	$('#upload-file-btn').click(function() {
		var form_data = new FormData($('#upload-file')[0]);
		$.ajax({
			type: 'POST',
			url: '/uploadajax',
			data: form_data,
			contentType: false,
			cache: false,
			processData: false,
			async: false,
			success: function(data) 
			{
				d = new Date();
				$('#image_preview img').attr("src", "svg/pattern.svg?"+d.getTime());
			},
		});
	});

	$('.command').click(function() 
	{
		var url = this.href;
		var attributes = $(this).data();
		$.ajax({
			type: "POST",
			url: url,
			data: attributes,
			success: function(msg)
			{
				console.log("ok");
			}
		});
		return false; // prevent default

		console.log(attributes);
	});
	
	var object = document.getElementsByTagName('object')[0];
	object.addEventListener('load', function(){
		scale_svg();
	});

	scale_svg();
}

function scale_svg()
{
	var svg = document.getElementsByTagName('object')[0].contentDocument.getElementsByTagName('svg')[0];
	var bbox = svg.getBBox();
	var viewBox = [bbox.x, bbox.y, bbox.width, bbox.height].join(" ");
	svg.setAttribute("viewBox", viewBox);	
	svg.viewBox = viewBox;
	
	svg.setAttribute("height", "100%");
	svg.setAttribute("width", "100%");
	svg.height = "100%";
	svg.height = "100%";
}