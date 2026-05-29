import React from 'react'
import { Layout } from './components/Layout'
import { ChatInterface } from './components/ChatInterface'
import { EvaluationPane } from './components/EvaluationPane'

function App() {
  return (
    <Layout>
      <div className="flex h-full overflow-hidden">
        <ChatInterface />
        <EvaluationPane />
      </div>
    </Layout>
  )
}

export default App
