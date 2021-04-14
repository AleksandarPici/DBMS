
## Term level upiti
GET /products/_search
{
  "query": {
    "term": {
      "name": "lobster"
    }
  }
}
```

```
GET /products/_search
{
  "query": {
    "term": {
      "name": "Lobster"
    }
  }
}

GET /products/_search
{
  "query": {
    "match": {
      "name": "Lobster"
    }
  }
}

# DSL upiti
GET /products/_search
{
  "query": {
    "match_all": {}
  }
}

# Request URI upiti

## Pretrazivanje svih dokumenata
GET /products/_search?q=*
```

## Samo koji sadrze Lobster u name
GET /products/_search?q=name:Lobster

## koji sadrze tag Meat
GET /products/_search?q=tags:Meat
```

## Koji sadrze tag meat i u imenu tuna
GET /products/_search?q=tags:Meat AND name:Tuna

## Razumevanje score
GET /products/_search
{
  "explain": true,
  "query": {
    "term": {
      "name": "lobster"
    }
  }
}

## debagiranje
GET /products/_doc/1/_explain
{
  "query": {
    "term": {
      "name": "lobster"
    }
  }
}