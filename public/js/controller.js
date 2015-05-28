var converter = angular.module('converter', ['ui.router']);

converter.controller('bodyCtrl', ['$scope', '$http', function($scope, $http) {

    $scope.done = false;

    $scope.convertDNA = function() {
        $http.post('http://localhost:9000/convertDNA', $scope.entry).success(function (data) {
            $scope.currentAA = data.aa;
            $scope.currentRNA = data.rna;
            $scope.done = true;
        });
    };

    $scope.entries;

    $scope.getdb = function() {
        $http.get('http://localhost:9000/getdb').success(
            function (data) {
                $scope.entries = data;
        });
    };

}]);

converter.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/convert');

    $stateProvider
        
    .state('convert', {
        url: '/convert',
        templateUrl: '../partials/convert.html'
    })
    
    .state('database', {
        url: '/database',
        templateUrl: '../partials/database.html'
    });  
});

// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
// Javascript
