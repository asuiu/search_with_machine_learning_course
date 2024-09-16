import json
a = '''"/product/productId/text()", "productId",
"/product/sku/text()", "sku",
"/product/name/text()", "name",
"/product/type/text()", "type",
"/product/startDate/text()", "startDate",
"/product/active/text()", "active",
"/product/regularPrice/text()", "regularPrice",
"/product/salePrice/text()", "salePrice",
"/product/onSale/text()", "onSale",
"/product/digital/text()", "digital",
"/product/frequentlyPurchasedWith/*/text()", "frequentlyPurchasedWith",
"/product/accessories/*/text()", "accessories",
"/product/relatedProducts/*/text()", "relatedProducts",
"/product/crossSell/text()", "crossSell",
"/product/salesRankShortTerm/text()", "salesRankShortTerm",
"/product/salesRankMediumTerm/text()", "salesRankMediumTerm",
"/product/salesRankLongTerm/text()", "salesRankLongTerm",
"/product/bestSellingRank/text()", "bestSellingRank",
"/product/url/text()", "url",
"/product/categoryPath/*/name/text()", "categoryPath", 
"/product/categoryPath/*/id/text()", "categoryPathIds", 
"/product/categoryPath/category[last()]/id/text()", "categoryLeaf",
"count(/product/categoryPath/*/name)", "categoryPathCount",
"/product/customerReviewCount/text()", "customerReviewCount",
"/product/customerReviewAverage/text()", "customerReviewAverage",
"/product/inStoreAvailability/text()", "inStoreAvailability",
"/product/onlineAvailability/text()", "onlineAvailability",
"/product/releaseDate/text()", "releaseDate",
"/product/shippingCost/text()", "shippingCost",
"/product/shortDescription/text()", "shortDescription",
"/product/shortDescriptionHtml/text()", "shortDescriptionHtml",
"/product/class/text()", "class",
"/product/classId/text()", "classId",
"/product/subclass/text()", "subclass",
"/product/subclassId/text()", "subclassId",
"/product/department/text()", "department",
"/product/departmentId/text()", "departmentId",
"/product/bestBuyItemId/text()", "bestBuyItemId",
"/product/description/text()", "description",
"/product/manufacturer/text()", "manufacturer",
"/product/modelNumber/text()", "modelNumber",
"/product/image/text()", "image",
"/product/condition/text()", "condition",
"/product/inStorePickup/text()", "inStorePickup",
"/product/homeDelivery/text()", "homeDelivery",
"/product/quantityLimit/text()", "quantityLimit",
"/product/color/text()", "color",
"/product/depth/text()", "depth",
"/product/height/text()", "height",
"/product/weight/text()", "weight",
"/product/shippingWeight/text()", "shippingWeight",
"/product/width/text()", "width",
"/product/longDescription/text()", "longDescription",
"/product/longDescriptionHtml/text()", "longDescriptionHtml",
"/product/features/*/text()", "features",'''
names = [s.split(',')[1].strip(' "') for s in a.split('\n')]
d = {
          "type": "text",
          "fields": {
            "keyword": {
              "type": "keyword",
              "ignore_above": 2048
            }
          }
        }
mapping = {name:d for name in names}

with open('names.map.json', 'w') as f:
    json.dump(mapping, f, indent=2)