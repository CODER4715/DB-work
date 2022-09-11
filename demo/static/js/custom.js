/*-------------------------------------------------------------------------
 * RENDIFY - Custom jQuery Scripts
 * ------------------------------------------------------------------------

	1.	Plugins Init
	2.	Site Specific Functions
	3.	Shortcodes
	4.      Other Need Scripts (Plugins config, themes and etc)
	
-------------------------------------------------------------------------*/
"use strict";

jQuery(document).ready(function($) {


	/*------------------------------------------------------------------------*/
	/*	1.	Plugins Init
	/*------------------------------------------------------------------------*/


	/************** Single Page Nav Plugin *********************/
	$('.menu').singlePageNav({
		filter: ':not(.external)'
	});




	/************** FlexSlider Plugin *********************/
	$('.flexslider').flexslider({
		animation: 'fade',
		controlNav: false,
		nextText: '',
		prevText: '',
	});

	$('.flex-caption').addClass('animated bounceInDown');

	$('.flex-direction-nav a').on('click', function() {
		$('.flex-caption').removeClass('animated bounceInDown');
		$('.flex-caption').fadeIn(0).addClass('animated bounceInDown');
	});


	/************** LightBox *********************/
	$(function() {
		$('[data-rel="lightbox"]').lightbox();
	});




	/*------------------------------------------------------------------------*/
	/*	2.	Site Specific Functions
	/*------------------------------------------------------------------------*/


	/************** Go Top *********************/
	$('#go-top').click(function(event) {
		event.preventDefault();
		jQuery('html, body').animate({
			scrollTop: 0
		}, 800);
		return false;
	});



	/************** Responsive Navigation *********************/
	$('.toggle-menu').click(function() {
		$('.menu').stop(true, true).toggle();
		return false;
	});
	$(".responsive-menu .menu a").click(function() {
		$('.responsive-menu .menu').hide();
	});






});

/***************** 时间选择框 ***************************/
$('#depart_date_modify,#depart_date_select,#date_buy,#depart_date_banci,#book_date').datetimepicker({
	forceParse: 0, //设置为0，时间不会跳转1899，会显示当前时间。
	language: 'zh-CN', //显示中文
	format: 'yyyy/mm/dd', //显示格式
	minView: 'month', //设置只显示到月份
	initialDate: new Date(), //初始化当前日期
	autoclose: true, //选中自动关闭
	todayBtn: true, //显示今日按钮
})
$("#depart_date_modify,#depart_date_select,#date_buy,#depart_date_banci,#book_date").datetimepicker("setDate", new Date()); //设置显示默认当天的时间


/******************* Ajax提交 *************************/
$('#addFlight').on('submit', function() {
	addFlightPost()
	event.preventDefault() //阻止form表单默认提交
})

function addFlightPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/addFlight/",
		data: $('#addFlight').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};

$('#delFlight').on('submit', function() {
	delFlightPost()
	event.preventDefault() //阻止form表单默认提交
})

function delFlightPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/delFlight/",
		data: $('#delFlight').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};




$('#flightModify').on('submit', function() {
			flightModifyPost()
			event.preventDefault() //阻止form表单默认提交
	})

function flightModifyPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/flightModify/",
		data: $('#flightModify').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};

$('#addcn').on('submit', function() {
	addcnPost()
	event.preventDefault() //阻止form表单默认提交
})

function addcnPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/AddCN/",
		data: $('#addcn').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};

$('#addfr').on('submit', function() {
	addfrPost()
	event.preventDefault() //阻止form表单默认提交
})

function addfrPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/AddFR/",
		data: $('#addfr').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};

$('#delBanci').on('submit', function() {
	delbanciPost()
	event.preventDefault() //阻止form表单默认提交
})

function delbanciPost() {
	$.ajax({
		type: "post",
		url: "http://127.0.0.1:5000/delbanci/",
		data: $('#delBanci').serialize(),
		dataType: 'text',
	}).success(function(message) {
		alert(message)
	}).fail(function(err) {
		alert(err)
	})
};




/******************** 多按钮提交到不同server*************/

    function buysub(){
		document.buy.action="http://127.0.0.1:5000/BuyTickets/";
    }
    function backsub() {
		document.buy.action="http://127.0.0.1:5000/ticketBack/";
	}
	
	function prevent(){
		event.preventDefault()
		$.ajax({
			type: "post",
			url: document.buy.action,
			data: $('#buy').serialize(),
			dataType: 'text',
		}).success(function(message) {
			alert(message)
		}).fail(function(err) {
			alert(err)
		})
	}