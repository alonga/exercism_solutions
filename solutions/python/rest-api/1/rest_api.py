import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database or {"users": []}

    def get_user(self, name):
        return next(u for u in self.database["users"] if u["name"] == name)

    def calculate_balance(self, user):
        user["balance"] = round(
            sum(user["owed_by"].values()) - sum(user["owes"].values()), 2
        )

    def clean_user(self, user):
        self.calculate_balance(user)
        return {
            "name": user["name"],
            "owes": dict(sorted(user["owes"].items())),
            "owed_by": dict(sorted(user["owed_by"].items())),
            "balance": user["balance"],
        }

    def get(self, url, payload=None):
        if url == "/users":
            if payload:
                names = json.loads(payload)["users"]
                users = [self.clean_user(self.get_user(n)) for n in names]
            else:
                users = [
                    self.clean_user(u)
                    for u in sorted(self.database["users"], key=lambda x: x["name"])
                ]
            return json.dumps({"users": users})

    def post(self, url, payload=None):
        data = json.loads(payload) if payload else {}

        if url == "/add":
            new_user = {
                "name": data["user"],
                "owes": {},
                "owed_by": {},
                "balance": 0.0,
            }
            self.database["users"].append(new_user)
            return json.dumps(self.clean_user(new_user))

        if url == "/iou":
            lender = self.get_user(data["lender"])
            borrower = self.get_user(data["borrower"])
            amount = data["amount"]

            # Net-out opposite direction using canonical "owes"
            if lender["name"] in borrower["owes"]:
                prev = borrower["owes"][lender["name"]]
                if prev > amount:
                    borrower["owes"][lender["name"]] = round(prev - amount, 2)
                    amount = 0
                else:
                    del borrower["owes"][lender["name"]]
                    amount = round(amount - prev, 2)

            elif borrower["name"] in lender["owes"]:
                prev = lender["owes"][borrower["name"]]
                if prev > amount:
                    lender["owes"][borrower["name"]] = round(prev - amount, 2)
                    amount = 0
                else:
                    del lender["owes"][borrower["name"]]
                    amount = round(amount - prev, 2)

            # Remaining → borrower owes lender
            if amount > 0:
                borrower["owes"][lender["name"]] = round(
                    borrower["owes"].get(lender["name"], 0) + amount, 2
                )

            # Rebuild owed_by from owes
            for user in [lender, borrower]:
                user["owed_by"] = {}
            for user in self.database["users"]:
                for debtor, amt in user["owes"].items():
                    creditor = user["name"]
                    if amt > 0:
                        other = self.get_user(debtor)
                        other["owed_by"][creditor] = amt

            users = sorted([lender, borrower], key=lambda u: u["name"])
            return json.dumps({"users": [self.clean_user(u) for u in users]})


# ---- TEST YOU REQUESTED ----

# Test Initial State
database = {
    "users": [
        {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
        {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
    ]
}

api = RestAPI(database)

payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 2.0})
response = api.post("/iou", payload)

expected = {
    "users": [
        {"name": "Adam", "owes": {"Bob": 1.0}, "owed_by": {}, "balance": -1.0},
        {"name": "Bob", "owes": {}, "owed_by": {"Adam": 1.0}, "balance": 1.0},
    ]
}

print("RESULT:  ", json.loads(response))
print("EXPECTED:", expected)

if json.loads(response) == expected:
    print("\n🎉 PASS: Output matches expected result!")
else:
    print("\n❌ FAIL: Output does NOT match expected result!")
