from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import plotly.graph_objs as go

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, slope: float = 1, intercept: float = 0):
    x_values = list(range(-10, 11))
    y_values = [slope * x + intercept for x in x_values]

    plot_data = [
        go.Scatter(x=x_values, y=y_values, mode='lines', name='Line'),
    ]
    layout = go.Layout(title="Plot", xaxis=dict(title="X"), yaxis=dict(title="Y"))

    fig = go.Figure(data=plot_data, layout=layout)
    plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return templates.TemplateResponse("index.html", {"request": request, "slope": slope, "intercept": intercept, "plot_html": plot_html})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
