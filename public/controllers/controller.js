var translator = angular.module('translator', []);

translator.controller('bodyCtrl', ['$scope', '$http', function($scope, $http) {

	$scope.done = false;

	$scope.convertAA = function() {
        $http.post('http://localhost:9000/convertAA', $scope.entry).success(function (data) {
            $scope.currentAA = data;
            console.log(data);
            $scope.done = true;
        });
    };

}]);
