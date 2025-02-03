import React, { useState } from "react";
import axios, { AxiosError } from "axios";
import MarkdownPreview from "@uiw/react-markdown-preview";
import { Loader } from "lucide-react";

const Form: React.FC = () => {
  const [prompt, setPrompt] = useState("");
  const [resData, setResData] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    if (prompt.trim() === "") {
      console.log("Please enter a prompt");
      return;
    }

    try {
      setIsLoading(true);
      const response = await axios.post("http://127.0.0.1:8000", {
        query: prompt,
      });

      setResData(response.data.data);
    } catch (error) {
      console.log(error);
      const err = error as AxiosError;
      setError(err.message);
    } finally {
      setIsLoading(false);
      setPrompt("");
    }
  };

  if (error) {
    return (
      <div className="flex items-center justify-center h-full">
        <h1 className="text-2xl font-bold text-red-500">{error}</h1>
      </div>
    );
  }

  return (
    <div className="flex gap-2 w-full h-full flex-col p-5">
      <div className="flex items-center gap-2">
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt..."
          className="px-4 text-white py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 w-full placeholder:text-white min-h-[100px]bg-transparent"
        />{" "}
        <button
          onClick={handleSubmit}
          className="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-50"
        >
          {isLoading ? <Loader className="h-5 w-5 animate-spin" /> : "Submit"}
        </button>
      </div>

      <div className="flex items-center justify-center mt-6 p-2">
        {isLoading ? (
          <div className="h-[40vh] w-full bg-gray-800/50 rounded-lg flex items-center justify-center gap-3">
            <Loader className="h-7 w-7 animate-spin" />
            <h1 className="text-xl font-bold text-gray-400"><span className="text-blue-600">Generating</span> The Response 🤖</h1>
          </div>
        ) : (
          resData && (
            <MarkdownPreview source={resData} style={{ padding: 16 }} />
          )
        )}
      </div>
    </div>
  );
};

export default Form;
