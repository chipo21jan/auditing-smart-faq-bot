// Direct Bedrock API calls from browser
// Note: This requires AWS credentials configured locally

import { BedrockAgentRuntimeClient, InvokeAgentCommand } from "@aws-sdk/client-bedrock-agent-runtime";

const client = new BedrockAgentRuntimeClient({ 
  region: "us-east-1"
});

export async function askAgent(question: string, sessionId: string) {
  const command = new InvokeAgentCommand({
    agentId: "BAUJICP7L10",
    agentAliasId: "WTVHMKDT5R",
    sessionId: sessionId,
    inputText: question,
    enableTrace: false
  });

  try {
    const response = await client.send(command);
    
    let answer = "";
    const stream = response.completion;
    
    if (stream) {
      for await (const event of stream) {
        if (event.chunk?.bytes) {
          const text = new TextDecoder().decode(event.chunk.bytes);
          answer += text;
        }
      }
    }
    
    return {
      answer: answer || "No response generated",
      citations: [],
      sessionId: sessionId
    };
  } catch (error) {
    console.error("Error calling Bedrock:", error);
    throw error;
  }
}
