function fetchUserData(userId, callback) {
    // simulate fetching user data from a database
    setTimeout(() => {
      const userData = { id: userId, name: 'Prajith', email: 'prajith@gmail.com' };
      callback(userData);
    }, 1000);
  }
  
  fetchUserData(123, (userData) => {
    console.log(userData);
  });