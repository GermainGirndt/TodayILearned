```
const json = {
    "components": [
        {
            "component": "section_page_hero",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "background_color": "rgb(255, 255, 255)",
                "background_image": {
                    "path": "https://cdn.melhorplano.net/cms/2019/08/23/5d603bf6b255fPage-Hero.svg",
                    "meta": {
                        "title": "Page hero background vetor"
                    }
                },
                "image_position": "Background",
                "components": [
                    {
                        "component": "title",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "text": "Compare planos de Internet Banda Larga",
                            "tag": "h1"
                        }
                    },
                    {
                        "component": "section_zip_form",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "components": [
                                {
                                    "component": "image",
                                    "settings": {
                                        "id": "",
                                        "class": "",
                                        "style": "",
                                        "image": {
                                            "path": "https://cdn.melhorplano.net/cms/2019/08/22/5d5ea234086beGroup-36default-hero-logo.svg",
                                            "meta": {
                                                "title": "Imagem Wifi"
                                            }
                                        },
                                        "width": null,
                                        "height": null
                                    }
                                },
                                {
                                    "component": "title",
                                    "settings": {
                                        "id": "",
                                        "class": "",
                                        "style": "",
                                        "text": "Veja a cobertura de internet banda larga na sua região",
                                        "tag": "h2"
                                    }
                                },
                                {
                                    "component": "button",
                                    "settings": {
                                        "id": "",
                                        "class": "",
                                        "style": "",
                                        "text": "Ver Disponibilidade",
                                        "url": "/internet-banda-larga/planos"
                                    }
                                }
                            ]
                        }
                    }
                ],
                "target": true
            }
        },
        {
            "component": "zip_toolbar",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "image": {
                    "path": "https://cdn.melhorplano.net/cms/2019/08/22/5d5ea14d4494cGroup-36.1default-toolbar.svg",
                    "meta": {
                        "title": "Imagem Wifi"
                    }
                },
                "background_color": "rgb(219, 239, 232)",
                "components": [
                    {
                        "component": "title",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "text": "Veja a cobertura exata em sua região.",
                            "tag": "h2"
                        }
                    },
                    {
                        "component": "button",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "text": "Ver Disponibilidade",
                            "url": "/internet-banda-larga/sp/sao-paulo"
                        }
                    }
                ]
            }
        },
        {
            "component": "breadcrumbs",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "links": [
                    {
                        "value": {
                            "anchor_text": "Internet Banda Larga",
                            "link": "/internet-banda-larga"
                        }
                    },
                    {
                        "value": {
                            "anchor_text": "Planos",
                            "link": "/internet-banda-larga/planos"
                        }
                    }
                ],
                "target": true
            }
        },
        {
            "component": "comparison",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "filters_collection": {
                    "_id": "5cc6f31e38383044be0002e4",
                    "description": "Filtros Banda Larga",
                    "filters": [
                        {
                            "component": "filter_multi_select",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Ver Planos",
                                "query_string_field": "t",
                                "api_field": null,
                                "static_values": [
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "Internet",
                                            "value": "broadband"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "Internet + TV",
                                            "value": "comboBroadbandTv"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "Internet + Fixo",
                                            "value": "comboBroadbandLandline"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "Internet + TV + Fixo",
                                            "value": "comboBroadbandTvLandline"
                                        }
                                    }
                                ],
                                "static_values_empty_default": true
                            }
                        },
                        {
                            "component": "filter_range",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Velocidade da Internet",
                                "first_label": "Ao menos",
                                "last_label": "Mega",
                                "default_value": "min",
                                "query_string_field": "bdmin",
                                "api_field": "broadbandDownload",
                                "static_values": null
                            }
                        },
                        {
                            "component": "filter_range",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Preço",
                                "first_label": "Até R$",
                                "last_label": null,
                                "default_value": "max",
                                "query_string_field": "pmax",
                                "api_field": "price",
                                "static_values": null
                            }
                        },
                        {
                            "component": "filter_multi_select",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Provedores",
                                "query_string_field": "ps",
                                "api_field": "provider",
                                "static_values": null
                            }
                        },
                        {
                            "component": "filter_select",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Pontos de TV",
                                "query_string_field": "tvc",
                                "api_field": null,
                                "static_values": [
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "1 Ponto",
                                            "value": 1
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "2 Pontos",
                                            "value": 2
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "3 Pontos",
                                            "value": 3
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "4 Pontos",
                                            "value": 4
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "item",
                                            "label": "Item",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "label",
                                                        "type": "text",
                                                        "label": "Label"
                                                    },
                                                    {
                                                        "name": "value",
                                                        "type": "text",
                                                        "label": "Valor"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "label": "5 Pontos",
                                            "value": 5
                                        }
                                    }
                                ]
                            }
                        }
                    ],
                    "_mby": "5bf4130938316607ac000287",
                    "_by": "5bf2ccee38316607ac000148",
                    "_modified": 1563200574,
                    "_created": 1556542238,
                    "_link": "filter_comparison"
                },
                "sort_collection": {
                    "_id": "5cc6f3783838303f1900028a",
                    "description": "Ordenação Banda Larga",
                    "sort": [
                        {
                            "component": "sort_item",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "selected": true,
                                "option": "Menor Preço;price;1"
                            }
                        },
                        {
                            "component": "sort_item",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "selected": null,
                                "option": "Mais Canais;tvNumberOfChannels;-1"
                            }
                        }
                    ],
                    "_mby": "5bf2ccee38316607ac000148",
                    "_by": "5bf2ccee38316607ac000148",
                    "_modified": 1564417385,
                    "_created": 1556542328,
                    "_link": "sort_comparison"
                },
                "segment": "b2c",
                "providers": null,
                "product_types": [
                    "broadband",
                    "comboBroadbandTv",
                    "comboBroadbandLandline",
                    "comboBroadbandTvLandline"
                ],
                "max_results": "20",
                "default_location": null,
                "plan_name": null,
                "min_price": null,
                "max_price": null,
                "min_broadband": null,
                "max_broadband": null,
                "min_mobile": null,
                "max_mobile": null,
                "lines_mobile": null,
                "mobile_minutes": null,
                "landline_minutes": null
            }
        },
        {
            "component": "zip_popover",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "zip_popover_collection": {
                    "_id": "5d5bfd568ac8635d82716832",
                    "description": "Zip Popover (test)",
                    "text": "Por favor, informe seu CEP para verificarmos os planos disponíveis no seu endereço.",
                    "_mby": "5bfb7b5c38316607ad000217",
                    "_by": "5bf4130938316607ac000287",
                    "_modified": 1566497725,
                    "_created": 1566309718,
                    "_link": "zip_popover"
                }
            }
        },
        {
            "component": "zip_modal",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "components": [
                    {
                        "component": "image",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "image": {
                                "path": "https://cdn.melhorplano.net/cms/2019/08/26/5d63f8e976396Group-36modal.svg",
                                "meta": {
                                    "title": "Imagem Wifi"
                                }
                            },
                            "width": null,
                            "height": null
                        }
                    },
                    {
                        "component": "title",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "text": "Veja a cobertura da sua região.",
                            "tag": "h2"
                        }
                    },
                    {
                        "component": "button",
                        "settings": {
                            "id": "",
                            "class": "",
                            "style": "",
                            "text": "Ver Disponibilidade",
                            "url": "/internet-banda-larga/planos"
                        }
                    }
                ]
            }
        },
        {
            "component": "footer_standard",
            "settings": {
                "id": "",
                "class": "",
                "style": "",
                "footer_collection": {
                    "_id": "5cbb3acb383830754f0000d2",
                    "description": "Footer Padrão",
                    "columns": [
                        {
                            "component": "footer_column",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Conheça",
                                "links": [
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Conheça o Comparador",
                                            "link": "/"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Blog",
                                            "link": "/blog/"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Sobre",
                                            "link": "/sobre"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "component": "footer_column",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Faça Parte",
                                "links": [
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Trabalhe Conosco",
                                            "link": "/vagas"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Seja um Parceiro",
                                            "link": "https://www.parcerias.melhorplano.net/"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "component": "footer_column",
                            "settings": {
                                "id": "",
                                "class": "",
                                "style": "",
                                "title": "Mais",
                                "links": [
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Sala de Imprensa",
                                            "link": "/sala-de-imprensa"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Fale Conosco",
                                            "link": "mailto:contato@melhorplano.net"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Política de Privacidade",
                                            "link": "/politica-de-privacidade"
                                        }
                                    },
                                    {
                                        "field": {
                                            "type": "set",
                                            "name": "link",
                                            "label": "Link",
                                            "options": {
                                                "fields": [
                                                    {
                                                        "name": "anchor_text",
                                                        "type": "text",
                                                        "label": "Anchor Text"
                                                    },
                                                    {
                                                        "name": "link",
                                                        "type": "text",
                                                        "label": "Link"
                                                    }
                                                ]
                                            }
                                        },
                                        "value": {
                                            "anchor_text": "Termos de Uso",
                                            "link": "/termo-de-uso"
                                        }
                                    }
                                ]
                            }
                        }
                    ],
                    "_mby": "5bfe882338316607ad0003ca",
                    "_by": "5bf2ccee38316607ac000148",
                    "_modified": 1570202070,
                    "_created": 1555774155,
                    "target": false,
                    "_link": "footer"
                }
            }
        }
    ],
    "_mby": "5bffdd7c38383038a300017e",
    "_by": "5bfb7b5c38316607ad000217",
    "_modified": 1573754854,
    "_created": 1566866578
}


console.log('-----------------------')

function findComponent ( componentArg ) {

  // initialyzing list
  let componentsList = "";

  // if JSON:
  // iterates over other keys and calls the function recursivelly
  // extracts 'component' key and return it
  if (typeof componentArg === 'object' && componentArg !== null) {

    if (componentArg["component"]) {
      componentsList = [...componentsList, componentArg["component"]]
    }   

    for (key in componentArg) {

      const moreComponents = findComponent(componentArg[key])

      if (moreComponents) {
        componentsList = [...componentsList, ...moreComponents]
      }
    }
    
    if (componentsList) {
      return componentsList
    }

  }


  // if array
  // iterates over elemenets
  // calls the function recursivelly
  if (Array.isArray(componentArg)) {


    for (arrayElement of componentArg) {

      const moreComponents = findComponent(arrayElement)

      if (moreComponents) {

        componentsList = [...componentsList, ...moreComponents]

      }

      if (componentsList) {
      return componentsList
     }
    }



  }



  
}

const content = findComponent(json)
console.log(content);

```
