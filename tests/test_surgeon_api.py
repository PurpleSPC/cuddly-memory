# import pytest
# from fastapi.testclient import TestClient


# # create surgeon

# new_surg = client.post("/surgeons/create", json={"name":"Dr Watson", "npi_no":None})

# assert new.status_code == 200

# # get surgeon by id#
# surg_id = new.json()["id"]    # gets the id# for the surgeon just created
# response = client.get(f"/surgeons/id/{surg_id}")

# assert response.status_code == 200
# data = response.json()   # format response to json
# assert data["id"] == surg_id
# assert data["name"] == "Dr Watson"