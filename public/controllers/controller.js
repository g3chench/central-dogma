var converter = angular.module('converter', []);

converter.controller('bodyCtrl', ['$scope', '$http', function($scope, $http) {

	$scope.dnadone = false;

	$scope.convertDNA = function() {
        $http.post('http://localhost:9000/convertAA', $scope.entry).success(function (data) {
            $scope.currentAA = data.aa;
            $scope.dnadone = true;
        });
    };

    $scope.entries;

    $scope.getdb = function() {
        $http.get('http://localhost:9000/getdb').success(
            function (data) {
                $scope.entries = data;
            })
    };

}]);
