window.onload = function() 
{	
	$('#button_cut').click(function() {
		$('.ui.modal')
		.modal({
			onApprove : function() {
				$.post( "/cut" );
				return false;
			}
		})
		.modal('show');
	});

	$(document).keydown(function(e) 
	{
		if($('.ui.modal').hasClass('active'))
		{
			switch(e.which) {
				case 32: // cut
				$.post( "/cut" );
				break;
				
				case 37: // left
				$.post( "/move", { direction: "W" } );
				break;

				case 38: // up
				$.post( "/move", { direction: "N" } );
				break;

				case 39: // right
				$.post( "/move", { direction: "E" } );
				break;

				case 40: // down
				$.post( "/move", { direction: "S" } );
				break;

				default: return; // exit this handler for other keys
			}
			e.preventDefault(); // prevent the default action (scroll / move caret)
		}

	});

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
				var json = JSON.parse(data);
				
				d = new Date();
				$('#image_preview object').attr("data", "svg/pattern.svg?"+d.getTime());
				$('#cut_preview object').attr("data", "svg/pattern.svg?"+d.getTime());
				
				$('#image_properties #width').text(json['width']+json['units']);
				$('#image_properties #height').text(json['height']+json['units']);
			},
		});
	});
	
	var object = document.getElementsByTagName('object')[0];
	object.addEventListener('load', function(){
		scale_svg();
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
	});
	
	$('input[type=range]').bind("propertychange change", function(event)
	{
		var name = $(this).attr("name");
		var input = $('input[name='+name+']');
		input.val(this.value);
	})
	
	$('.setting').bind("propertychange change input", function(event)
	{
		var name = $(this).attr("name")
		var value = $(this).val()
		
		if($.isNumeric(value))
		{
			var slider = $('input[type=range][name='+name+']');
			slider.val(this.value);
		
			$.ajax({
				type: "POST",
				url: "/setting",
				data: { setting:name, value:value },
				success: function(msg)
				{
					console.log("ok");
				}
			});
		}
		return false; // prevent default
	});
	
	$('.ui.accordion').accordion();	
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