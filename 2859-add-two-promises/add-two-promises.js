var addTwoPromises = async function(promise1, promise2) {
    const [n1, n2] = await Promise.all([promise1, promise2]);
    return n1 + n2;
};
