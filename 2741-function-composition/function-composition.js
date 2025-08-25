var compose = function(functions) {
    return function(x) {
        let y = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            y = functions[i](y);
        }
        return y;
    };
};
