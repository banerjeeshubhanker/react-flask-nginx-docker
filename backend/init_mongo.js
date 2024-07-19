
db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

db = db.getSiblingDB("helloworlddb");

db.createCollection('messages', { capped: false });

db.messages.insertOne({
  type: "greeting",
  text: "Hello World"
});
