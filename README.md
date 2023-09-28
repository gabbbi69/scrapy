# scrapy
proyecto de scrapy
uno de los principales problemas, es que con los videotutoriales de youtube
no te devuelve los resultados sale erro 403, denegando el acceso a la pagina
mediante scrapy, debido que a ahora en 2023 se a implementado
metodos para evitar el scrapy, para solucionar esto se uso

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
en el archivo settings

con esta modificacion ahora si devuelve los resultados
asi mismo se cambio las etiquetas de los precios y titulos por lo siguiente:

"precio": response.xpath('//span[@class="andes-money-amount__fraction"]/text()').getall(),
"titulo": response.xpath('//h2[@class="ui-search-item__title shops__item-title"]/text()').getall(),
        
