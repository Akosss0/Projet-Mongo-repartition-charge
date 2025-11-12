// init-shard.js
rs.initiate({
    _id: "principal_a",
    members: [
        { _id: 0, host: "principal_a:27019" }, //Principal a
        { _id: 1, host: "secondaire_a_1:27020" }, //Secondaire_a_1
        { _id: 2, host: "secondaire_a_2:27021" }, //Secondaire_a_2
        { _id: 3, host: "secondaire_a_3:27022" } //Secondaire_a_3
    ]
});

rs.initiate({
    _id: "principal_b",
    members: [
        { _id: 0, host: "principal_b:27023" }, //Principal a
        { _id: 1, host: "secondaire_b_1:27024" }, //Secondaire_a_1
        { _id: 2, host: "secondaire_b_2:27025" }, //Secondaire_a_2
        { _id: 3, host: "secondaire_b_3:27026" } //Secondaire_a_3
    ]
});