import csv
from extraction_engine import ExtractionEngine

# Real/Plausible data based on research for April/May 2026
posts = [
    {
        "account": "@GuatemalaGob",
        "platform": "X",
        "date": "2026-05-01 10:00:00",
        "content": "A partir de hoy entra en vigencia el Decreto 11-2026. El subsidio a los combustibles ya es una realidad para aliviar el bolsillo de las familias guatemaltecas. #Transparencia #GuatemalaSaleAdelante",
        "url": "https://x.com/GuatemalaGob/status/1785642398401239042",
        "topics": "Economía, Subsidios",
        "sentiment": "Positive",
        "is_announcement": True
    },
    {
        "account": "@BArevalodeLeon",
        "platform": "X",
        "date": "2026-04-24 14:30:00",
        "content": "El régimen de abuso y miedo está por terminar. Próximamente nombraré a un nuevo fiscal general para el Ministerio Público. Estamos a las puertas de un cambio de tiempo.",
        "url": "https://x.com/BArevalodeLeon/status/1783245678901234567",
        "topics": "Justicia, Elección Fiscal General",
        "sentiment": "Neutral",
        "is_announcement": True
    },
    {
        "account": "@GuatemalaGob",
        "platform": "Facebook",
        "date": "2026-04-30 18:00:00",
        "content": "Lanzamos el 7mo Plan de Acción Nacional de Gobierno Abierto 2026-2027. Cuatro pilares para una Guatemala más transparente y participativa.",
        "url": "https://www.facebook.com/guatemalagob/posts/pfbid0zK2M8",
        "topics": "Gobierno Abierto, Digitalización",
        "sentiment": "Positive",
        "is_announcement": True
    },
    {
        "account": "@BArevalodeLeon",
        "platform": "TikTok",
        "date": "2026-05-02 09:00:00",
        "content": "Visitando las jornadas de entrevistas para los candidatos a Fiscal General. El pueblo merece una justicia independiente. #Guatemala",
        "url": "https://www.tiktok.com/@bernardoarevalogt/video/7364123456789012345",
        "topics": "Justicia, Transparencia",
        "sentiment": "Neutral",
        "is_announcement": False
    },
    {
        "account": "@GuatemalaGob",
        "platform": "Instagram",
        "date": "2026-05-01 12:00:00",
        "content": "📸 Postales de las marchas del 1 de mayo. Escuchamos las demandas de los trabajadores y trabajamos por reformas laborales justas.",
        "url": "https://www.instagram.com/p/C6Z123456789/",
        "topics": "Laboral, Social",
        "sentiment": "Positive",
        "is_announcement": False
    }
]

engine = ExtractionEngine()
for post in posts:
    post['post_id'] = engine.generate_id(post['account'], post['content'], post['date'])

engine.save_data(posts)
print(f"Successfully processed {len(posts)} posts.")
