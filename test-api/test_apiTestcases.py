from playwright.sync_api import sync_playwright, expect
import pytest

# @pytest.mark.api
def test_getApi(playwright):
    # context = playwright.request.new_context(http_credentials={"username":"us", "password":"pw"})
    context = playwright.request.new_context()
    response1 = context.get("https://dummyjson.com/products")
    response1 = 1234
    response = context.get("https://dummyjson.com/products", params={"limit":5}, headers={"Authorization": f"Bearer ${response1}"})
    # print(response.json())
    # print(response.status)
    # print(response.status_text)
    assert response.status==200
    jsonData = response.json()
    for i in range(0, jsonData["products"]):
        print(i["title"])
    # assert jsonData["products"][0]["title"]=="Essence Mascara Lash Princess"


# @pytest.mark.api
def test_postAPI(playwright):
      context = playwright.request.new_context()

      body = {
            "title": "Gaming Chair",
            "price": 299.99,
            "brand": "DXRacer"
            }
      headerValues ={"Authorization": "Bearer 1234"}

      response = context.post("https://dummyjson.com/products/add", headers=headerValues, data=body)
      assert response.status==201
      jsonresponse = response.json()
    #   jsonresponse = {
    #             "id": 195,
    #             "title": "Gaming Chair",
    #             "price": 299.99,
    #             "brand": "DXRacer"
    #         }
      print(jsonresponse["id"])


