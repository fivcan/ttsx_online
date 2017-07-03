$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var $name = $('#user_name');
		var len = $name.val().length;
		if(len<5||len>20)
		{
			$name.next().html('请输入5-20个字符的用户名');
			$name.next().css({'color':'#e62e2e'});
			$name.next().show();
			error_name = true;
		}
		else
		{
			$('#user_name').next().hide();
			$.get('/user_center/is_registed/', {'user_name': $name.val()}, function (data) {
			if(data == 'exist'){
				$name.next().html('用户名已存在, 请更换新的用户名');
				$name.next().css({'color':'#e62e2e'});
				$name.next().show();
				error_name = true;
			}else{
				$name.next().html('用户名可以注册');
				$name.next().show();
				$name.next().css({'color':'green'});
				error_name = false;
			}
        })
		}


	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#register_submit').click(function(){
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();
		// alert([error_name,error_password,error_check_password,error_email])
		if(error_name == true || error_password == true || error_check_password == true || error_email == true || error_check == true)
		{
			return false;
		}

	})




});