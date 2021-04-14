# Full text

```
GET /recipe/_search
{
  "query": {
    "multi_match": {
      "query": "pasta",
      "fields": [ "title", "description" ]
    }
  }
}
```

GET /recipe/_search
{
  "query": {
    "match_phrase": {
      "title": "spaghetti puttanesca"
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "match_phrase": {
      "title": "puttanesca spaghetti"
    }
  }
}


# novi podaci
curl -H "Content-Type: application/x-ndjson" -XPOST "http://localhost:9200/recipe/_bulk?pretty" --data-binary "@recipes-bulk.json"


GET /recipe/_mapping

GET /recipe/_search
{
  "query": {
    "match": {
      "title": "Recipes with pasta or spaghetti"
    }
  }
}
```

GET /recipe/_search
{
  "query": {
    "match": {
      "title": {
        "query": "Recipes with pasta or spaghetti",
        "operator": "and"
      }
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "match": {
      "title": {
        "query": "pasta or spaghetti",
        "operator": "and"
      }
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "match": {
      "title": {
        "query": "pasta spaghetti",
        "operator": "and"
      }
    }
  }
}
```
GET /recipe/_search
{
  "query": {
    "match": {
      "title": "Pasta with parmesan and spinach"
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "match_phrase": {
      "title": "pasta carbonara"
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "match_phrase": {
      "title": "carbonara pasta"
    }
  }
}
```

```
GET /recipe/_search
{
  "query": {
    "multi_match": {
      "query": "pasta pesto",
      "fields": [ "title", "description" ]
    }
  }
}
```