/**
 * Created by MostaK on 5/7/2017.
 */
///<reference path="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"/>


    var myApp = angular.module('myModule', []);
	myApp.controller('myController', function($scope, $http){

        $http.get('http://127.0.0.1:8000/rest/contacts/')

            .success (function(data){
                $scope.contacts = data;
					})
				.error(function(data, status) {
  						console.error('failure loading the student record', status, data);
  						$scope.contacts = { };
				});


	});

	var app = angular.module("myModule2", ["ngRoute"]);
app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "index.html"
    });
});






