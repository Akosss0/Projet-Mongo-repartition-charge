// init_shards.js : contient les trois definitions, mais on exécutera la partie correspondante
print('Helper script pour initialiser rsA/rsB/rsC. Charger la section voulue.');

// Exemple pour rsA (à exécuter dans principal_a)
function init_rsA(){
  rs.initiate({
    _id: "rsA",
    members: [
      { _id: 0, host: "principal_a:27017" },
      { _id: 1, host: "secondaire_a_1:27017" },
      { _id: 2, host: "secondaire_a_2:27017" },
      { _id: 3, host: "secondaire_a_3:27017" }
    ]
  });
}

// Exemple pour rsB (à exécuter dans principal_b)
function init_rsB(){
  rs.initiate({
    _id: "rsB",
    members: [
      { _id: 0, host: "principal_b:27017" },
      { _id: 1, host: "secondaire_b_1:27017" },
      { _id: 2, host: "secondaire_b_2:27017" },
      { _id: 3, host: "secondaire_b_3:27017" }
    ]
  });
}

// Exemple pour rsC (à exécuter dans principal_c)
function init_rsC(){
  rs.initiate({
    _id: "rsC",
    members: [
      { _id: 0, host: "principal_c:27017" },
      { _id: 1, host: "secondaire_c_1:27017" },
      { _id: 2, host: "secondaire_c_2:27017" },
      { _id: 3, host: "secondaire_c_3:27017" }
    ]
  });
}

print('-> Charger init_rsA(), init_rsB() ou init_rsC() selon le primaire en cours.');