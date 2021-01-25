ui = bootstrapPage(fluidPage(
    titlePanel('Web-based nomogram for predicting intracranial injury of TBI in children'),
    titlePanel('Tunthanathip et al.'),
    
    sidebarLayout(sidebarPanel(uiOutput('manySliders'),
                               uiOutput('setlimits'),
                               actionButton('add', 'Predict',class="btn-warning"),
                               br(), br(),
                               helpText('Press Quit to exit the application'),
                               actionButton('quit', 'Quit',class="btn-danger")
    ),
    mainPanel(tabsetPanel(id = 'tabs',
                          tabPanel('Graphical Summary', plotlyOutput('plot')),
                          tabPanel('Numerical Summary', verbatimTextOutput('data.pred'))
                          #tabPanel('Numerical Summary', verbatimTextOutput('data.pred')),
                          #tabPanel('Model Summary', verbatimTextOutput('summary'))
    )
    )
    )))
