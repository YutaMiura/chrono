// coding: utf-8
/* 
 * arp_calendarで使用するAjax等のJavaScript
*/
function getMinOptionValue(name) {
  var options = $(name).children();
  var min_value = 9999;
  for (var i = 0; i < options.length; i++) {
    var option = $(options)[i];
    var optVal = Number($(option).val());
    if (min_value > optVal) {
      min_value = optVal;
    }
  }
  return min_value;
}

function getMaxOptionValue(name) {
  var options = $(name).children();
  var max_value = 0;
  for (var i = 0; i < options.length; i++) {
    var option = $(options)[i];
    var optVal = Number($(option).val());
    if (max_value < optVal) {
      max_value = optVal;
    }
  }
  return max_value;
}

function getPrevMonthDate(year, month) {
  year = Number(year);
  month = Number(month);
  var result;
  if (month > getMinOptionValue("#select_month")) {
    result = new Date(year, month - 2);
  } else {
    if (year > getMinOptionValue("#select_year")) {
      result = new Date(year - 1, getMaxOptionValue("#select_month") - 1);
    } else {
      result = new Date(
        getMinOptionValue("#select_year"),
	getMinOptionValue("#select_month") - 1
      );
    }
  }
  return result;
}

function getNextMonthDate(year, month) {
  year = Number(year);
  month = Number(month);
  var result;
  if (month < getMaxOptionValue("#select_month")) {
    result = new Date(year, month);
  } else {
    if (year < getMaxOptionValue("#select_year")) {
      result = new Date(year + 1, getMinOptionValue("#select_month") - 1);
    } else {
      result = new Date(
        getMaxOptionValue("#select_year"),
	getMaxOptionValue("#select_month") - 1
      );
    }
  }
  return result;
}

$(function(){
  $("#prev_month").click(function(){
    prev_month_date = getPrevMonthDate($("#select_year").val(), $("#select_month").val());
    $("#select_year").val(prev_month_date.getFullYear());
    $("#select_month").val(prev_month_date.getMonth() + 1);
    $("#list_calendar").submit();
  });
  $("#next_month").click(function(){
    next_month_date = getNextMonthDate($("#select_year").val(), $("#select_month").val());
    $("#select_year").val(next_month_date.getFullYear());
    $("#select_month").val(next_month_date.getMonth() + 1);
    $("#list_calendar").submit();
  });
});
