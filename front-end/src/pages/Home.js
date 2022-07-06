import React from "react";
import Table from '../components/Table'
import Header from "../components/Header";
import Footer from "../components/Footer";
import InsertBar from "../components/InsertBar";

function Home() {
  return (
    <div className="container">      
      <Header h1="TAREFAS"/>
      <main>
        <InsertBar />
        <Table />
      </main>
      <Footer name={`${new Date().getFullYear()} Thiago`}/>
    </div>
  );
}

export default Home;
